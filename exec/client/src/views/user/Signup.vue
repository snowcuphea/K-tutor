<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn icon class="goToLogin" @click="goToLogin">
          <v-icon>mdi-close</v-icon>
        </v-btn>

      </v-col>
    </v-row>

    <v-row>
      <v-col class="d-flex justify-center">
        <h1> Signup </h1>
      </v-col>
    </v-row>

    <v-form ref="form" lazy-validation>
      <v-row style="height:60vh" class="d-flex align-center">
        <v-col>

          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Email" :rules="rulesEmail" hide-details="auto" type="text"
                v-model="signupCredentials.userEmail">
              </v-text-field>
            </v-col>
          </v-row>

          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Nickname" :rules="rulesNickname" hide-details="auto"
                v-model="signupCredentials.userNickname"></v-text-field>
            </v-col>
          </v-row>


          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Password" :rules="rulesPassword" hide-details="auto" type="password"
                v-model="signupCredentials.userPassword"></v-text-field>
            </v-col>
          </v-row>


          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Password Confirm" :rules="passwordConfirmation" hide-details="auto" type="password"
                v-model="signupCredentials.userPasswordConfirm"></v-text-field>
            </v-col>
          </v-row>



          <v-row class="mx-5 my-5">
            <v-col>
              <v-btn block large @click="signup">SIGNUP</v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
  import {
    signUp
  } from "@/api/account.js"

  export default {
    name: 'Signup',
    data: () => ({
      rulesEmail: [
        value => !!value || 'Required.',
        value => /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/.test(value) ||
        'Confirm your Email.',
      ],
      rulesPassword: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],

      rulesNickname: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      signupCredentials: {
        userEmail: "",
        userPassword: "",
        userPasswordConfirm: "",
        userNickname: "",

      }

    }),

    methods: {
      signup() {
        if (this.$refs.form.validate()) {

          signUp(
            this.signupCredentials,
            (res) => {
              console.log(res)
              console.log("signup Success")
              // alert("You joined Malmoong-chi successfully! (´▽`ʃ♥ƪ)")
              const alertInfo = {
                status: true,
                color: "success",
                icon: "mdi-home",
                content: "You joined Malmoong-chi successfully! (´▽`ʃ♥ƪ)"
              }
              this.$store.dispatch("showAlert", alertInfo)

              this.signupCredentials.userEmail = ''
              this.signupCredentials.userPassword = ''
              this.signupCredentials.userPasswordConfirm = ''
              this.signupCredentials.userNickname = ''
              this.$router.push({
                name: "Login"
              })
            },
            (err) => {
              // console.log("회원가입실패", err)
              if (err.response.status != undefined) {
                // alert(err.response.data)
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
          console.log("signup fail..")
        }

      },

      goToLogin() { //뒤로가기
        this.$router.go(-1)
      }
    },
    created() {

      this.signupCredentials.userEmail = ""
      this.signupCredentials.userPassword = ""
      this.signupCredentials.userPasswordConfirm = ""
      this.signupCredentials.userNickname = ""


    },
    computed: {
      passwordConfirmation() {
        return [
          value => value === this.signupCredentials.userPassword || 'Confirm your password.'
        ]
      },
    }
  }
</script>

<style>

</style>