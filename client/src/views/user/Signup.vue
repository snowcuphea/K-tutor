<template>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          icon
          class="goToLogin"
          @click="goToLogin"
        >
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
                v-model="userCredentials.userEmail">
              </v-text-field>
            </v-col>
          </v-row>

          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Nickname" :rules="rulesNickname" hide-details="auto"
                v-model="userCredentials.userNickname"></v-text-field>
            </v-col>
          </v-row>


          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Password" :rules="rulesPassword" hide-details="auto" type="password"
                v-model="userCredentials.userPassword"></v-text-field>
            </v-col>
          </v-row>

          
          <v-row class="mx-5">
            <v-col>
              <v-text-field label="Password Confirm" :rules="passwordConfirmation" hide-details="auto" type="password"
                v-model="userCredentials.userPasswordConfirm"></v-text-field>
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
  // import axios from "axios"

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
      userCredentials: {
        userEmail: "",
        userPassword: "",
        userPasswordConfirm: "",
        userNickname: "",

      }


    }),
    created() {

    },
    methods: {
      signup() {
        if (this.$refs.form.validate()) {
          console.log("signup Success")
          this.$router.push({
                name: "Login"
              })

          // let signupInfo = {
          //   username: this.userCredentials.userEmail,
          //   password: this.userCredentials.userPassword,
          //   nickname: this.userCredentials.userNickname,
          // }
          // console.log(signupInfo)
          // axios.post("http://localhost:8080/asdf/signup", signupInfo)
          //   .then(res => {
          //     console.log(res)
          //     alert("회원가입 성공")
          //     this.$router.push({
          //       name: "Login"
          //     })
          //     this.userCredentials.userEmail = ''
          //     this.userCredentials.userPassword = ''
          //     this.userCredentials.userNickname = ''
          //   })
          //   .catch((err) => {
          //     console.log(err)
          //     alert("회원가입 정보가 올바르지 않습니다.")
          //   })



        } else {
          console.log("signup fail..")
        }




      },

      goToLogin() { //뒤로가기
        this.$router.go(-1)
      }

    },
    computed: {
      passwordConfirmation() {
        return [
          value => value === this.userCredentials.userPassword || 'Confirm your password.'
        ]
      },
    }
  }
</script>

<style>

</style>