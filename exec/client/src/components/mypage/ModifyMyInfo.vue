<template>
  <div>
    <v-dialog v-model="showModifyMyInfo" fullscreen>
      <v-card width="100%" height="100%" tile>

        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Information </h2>
        <v-btn icon class="close-dialog" @click="[myInfoReset(), hideDialog()]">
          <v-icon>mdi-close</v-icon>
        </v-btn>

        <v-form ref="form" lazy-validation>
          <v-row style="height:60vh" class="d-flex align-center">
            <v-col>

              <v-row class="mx-5 d-flex align-center">
                <v-col cols="4" style="padding-bottom: 0">
                  <h4>
                    Nickname:
                  </h4>
                </v-col>
                <v-col>
                  <v-text-field label="Nickname" :rules="rulesNickname" hide-details="auto"
                    v-model="userCredentials.userNickname"></v-text-field>
                </v-col>

              </v-row>
              <v-row class="mx-5 d-flex align-center">
                <v-col cols="4" style="padding-bottom: 0">
                  <h4>
                    Password:
                  </h4>
                </v-col>
                <v-col>
                  <v-text-field label="Password" :rules="rulesPassword" hide-details="auto" type="password"
                    v-model="userCredentials.userPassword"></v-text-field>
                </v-col>

              </v-row>
              <v-row class="mx-5 d-flex align-center">
                <v-col cols="4" style="padding-bottom: 0">
                  <h4>
                    Password Confirm:
                  </h4>
                </v-col>
                <v-col>
                  <v-text-field label="Password Confirm" :rules="passwordConfirmation" hide-details="auto"
                    type="password" v-model="userCredentials.userPasswordConfirm"></v-text-field>
                </v-col>

              </v-row>
              <v-row>
                <v-col class="d-flex justify-end mr-7">
                  <v-btn class="main-bg-color-imp" dark @click="modify">Modify</v-btn>
                </v-col>
              </v-row>


            </v-col>
          </v-row>
        </v-form>
        <v-divider></v-divider>
        <v-container>
          <v-row class="pt-2">
            <v-subheader class="yourName">What is Your Joseon Name in Joseon Dynasty</v-subheader>
          </v-row>
          <v-row>
            <v-col cols="4" class="py-0">
              <v-subheader>
                Month
              </v-subheader>
            </v-col>
            <v-col cols="4" class="py-0">
              <v-subheader>
                Day
              </v-subheader>
            </v-col>
          </v-row>
          <v-row class="d-flex align-center my-0">
            <v-col cols="4" class="py-0">
              <v-select v-model="select_month" :items="items_month" class="py-0">

              </v-select>
            </v-col>
            <v-col cols="4" class="py-0">
              <v-select v-model="select_day" :items="items_day" class="py-0">

              </v-select>
            </v-col>
            <v-col cols="2">
              <v-btn class="main-bg-color-imp py-0" dark @click="search_name">Search</v-btn>
            </v-col>
          </v-row>
          <v-row v-if="nameVisible">
            <h3 class="ml-3">Your Korean nickname is {{ select_name_month[select_month-1] }}
              {{ select_name_day[select_day-1] }}.
            </h3>
          </v-row>
        </v-container>


      </v-card>

    </v-dialog>
  </div>

</template>

<script>
  import {
    updateUser
  } from "@/api/account.js"
  import {
    mapState
  } from 'vuex'

  export default {
    props: ['showModifyMyInfo'],
    data: () => ({
      rulesPassword: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      rulesNickname: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      userCredentials: {
        userNickname: "",
        userPassword: "",
        userPasswordConfirm: "",
      },
      items_month: [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
      ],
      items_day: [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31
      ],
      select_month: '',
      select_day: '',
      select_name_month: [
        'Ssang', 'Shea', 'Bok', 'Dol', 'Pang', 'Yuk', 'Ssang', 'Gae', 'Chil', 'Gap', 'Sam', 'Bang'
      ],
      select_name_day: [
        'Bong', 'Gu', 'Yok', 'Po', 'Ddong', 'Sam', 'Sik', 'Suk', 'Nom', 'Nim', 'Nyon', 'Dol', 'Dan', 'Dyuke',
        'Bang', 'Jil', 'Jang', 'Gul', 'Lae', 'Lyong', 'Dong', 'Soon', 'Ja', 'Bark', 'Chang', 'Un', 'Gut', 'Po',
        'Maan', 'Dan', 'Guk'
      ],
      nameVisible: false,

    }),
    methods: {
      hideDialog() {
        this.$emit('hideTutorial')
      },
      modify() {
        if (this.$refs.form.validate()) {


          updateUser(
            this.userCredentials,
            (res) => {
              this.$store.dispatch('updateUserInfo', res.data)
              console.log("update??", res.data)
              const alertInfo = {
                status: true,
                color: "success",
                icon: "mdi-home",
                content: "The information has been modified successfully."
              }
              this.$store.dispatch("showAlert", alertInfo)
              this.userCredentials.userPassword = ''
              this.userCredentials.userPasswordConfirm = ''
              this.hideDialog()

            },
            (err) => {
              console.log(err)
              if (err.response.status != undefined) {
                console.log(err.response.data)
                const alertInfo = {
                  status: true,
                  color: "error",
                  content: err.response.data
                }
                this.$store.dispatch("showAlert", alertInfo)
              }
            }
          )

        } else {
          console.log("failed modify info")
        }

      },
      myInfoReset() {
        // this.userCredentials.userNickname = this.nickName
        this.userCredentials.userNickname = ''
        this.userCredentials.userPassword = ''
        this.userCredentials.userPasswordConfirm = ''
      },
      search_name() {
        if (this.select_month != '' && this.select_day != '') {
          if (this.select_month == 2) {
            if (this.select_day < 29) {
              this.nameVisible = !this.nameVisible
            }
          } else if (this.select_month in [4, 6, 9, 11]) {
            if (this.select_day < 31) {
              this.nameVisible = !this.nameVisible
            }

          } else {
            this.nameVisible = !this.nameVisible
          }
        }
      }
    },
    computed: {
      passwordConfirmation() {
        return [
          value => value === this.userCredentials.userPassword || 'Confirm your password.'
        ]
      },
      ...mapState(["nickName"])
    },
    created() {
      this.userCredentials.userNickname = this.nickName
    }
  }
</script>

<style>
  .yourName {
    font-weight: bolder;
  }
</style>