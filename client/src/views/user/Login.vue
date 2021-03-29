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
              v-model="userCredentials.userPassword"></v-text-field>
          </v-col>
        </v-row>
        <v-row class="mx-5 my-5">
          <v-col>
            <v-btn block large>LOGIN</v-btn>
            <v-divider></v-divider>
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
      }
    }),

    methods: {

      login() {
        this.$store.dispatch("Login", this.userCredentials)
          .then(() => {
            this.$router.push({
              name: 'Report'
            })
            this.userCredentials.userEmail = ""
            this.userCredentials.userPassword = ""
          })
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