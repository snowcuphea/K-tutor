<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center mt-13">
        <h1> Login </h1>
      </v-col>
    </v-row>


    <v-row style="height:60vh" class="d-flex align-center">
      <v-col>

        <v-row class="mx-5 my-5">
          <v-col>
            <h2 class="float-left ml-3">Welcome to</h2>
            <h1 class="float-right main-background-color">Malmoong-Chi</h1>
          </v-col>
        </v-row>


        <v-row class="mx-5">
          <v-col>
            <v-text-field label="Email" :rules="rulesEmail" hide-details="auto" v-model="userCredentials.userEmail">
            </v-text-field>
          </v-col>
        </v-row>

        <v-row class="mx-5">
          <v-col>
            <v-text-field label="Password" :rules="rulesPassword" hide-details="auto" type="password"
              v-model="userCredentials.userPassword" @keyup.enter="login"></v-text-field>
          </v-col>
        </v-row>
        <v-row class="mx-5 my-5">
          <v-col>
            <v-btn block large @click="login">LOGIN</v-btn>
            <div class="d-flex justify-space-between my-2">
              <span @click="goToSignup">Join</span>
              <span @click="goToFindPassword">forgot password</span>
            </div>

          </v-col>
        </v-row>
      </v-col>
    </v-row>


    <!-- <v-row class="mx-5" >
      <v-col class="d-flex justify-space-between">
        <span>Join</span>
        <span>I forgot my password</span>
      </v-col>
    </v-row> -->


  </v-container>
</template>

<script>
  import { getToken, getInfo } from "@/api/account.js"
  import { getClassList } from "@/api/klass.js"

  export default {
    name: "Login",
    data: () => ({
      rulesEmail: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      rulesPassword: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      userCredentials: {
        userEmail: "",
        userPassword: "",
      },
    }),

    methods: {
      
      login() {
        localStorage.setItem("jwt", "")

        getToken(
          this.userCredentials,
          (response) => {
            localStorage.setItem("jwt", response.data.token)
            
            getInfo(
              (response) => {
                // console.log("레포트정보", response.data)
                this.$store.dispatch('addUserEmail', this.userCredentials.userEmail )
                this.$store.dispatch('setTime')
                this.userCredentials.userEmail = ""
                this.userCredentials.userPassword = ""

                this.$store.dispatch('getReportInfo', response.data)
                this.$store.dispatch('getAchievementList')
                this.$store.dispatch( 'getTestGrades' )
                
              },
              (error) => {
                console.log("account/login 에러", error)
              }
            )
            getClassList(
              (response) => {
                // console.log("로긴하고나서 getClassList 이제 dispatch해야징",response.data)
                this.$store.dispatch('getClassList', response.data)
              
              },
              (error) => {
                console.log("클래스 리스트를 가져오지 못하였어...",error)
              }
            )
            this.$router.push({name:'Home'})
            this.$store.state.currentPage = 'Report'
          },
          (error) => {
            console.log(error)
            const alertInfo = {
              status: true,
              color: "error",
              content: "Please check your Email or Password."
            }
            this.$store.dispatch("showAlert", alertInfo)
            // alert("Please check your Email or Password.")
          }

        )
      },

      goToSignup() {
        this.$router.push({
          name: 'Signup'
        })
      },

      goToFindPassword() {

      },
    }


  }
</script>

<style>


</style>