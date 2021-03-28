<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center">
        <h1> Login </h1>
      </v-col>
    </v-row>


    <v-row style="height:60vh" class="d-flex align-center">
      <v-col>

      <v-row class="mx-5">
        <!-- <v-col cols="4" class="d-flex align-end justify-end">
        <span>Email :</span>
      </v-col> -->
        <v-col>
          <v-text-field label="Email" :rules="rulesEmail" hide-details="auto" v-model="userCredentials.userEmail">
          </v-text-field>
        </v-col>
      </v-row>
      <v-row class="mx-5">
        <!-- <v-col cols="4" class="d-flex align-end justify-end">
        <span >Password :</span>
      </v-col> -->
        <v-col>
          <v-text-field label="Password" :rules="rulesPassword" hide-details="auto"
            v-model="userCredentials.userPassword"></v-text-field>
        </v-col>
      </v-row>
      <v-row class="mx-5 my-5">
        <v-col>
          <v-btn block large>LOGIN</v-btn>
          <div class="d-flex justify-space-between my-2">
            <a href="#" @click="goToSignup">Join</a>
            <a href="#" @click="goToFindPassword">forgot password</a>
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

      login: function () {
        this.$store.dispatch("LOGIN", this.userCredentials)
          .then(() => {
            this.$router.push({
              name: 'Report'
            })
            this.userCredentials.userEmail = ""
            this.userCredentials.userPassword = ""
          })
      },

      goToSignup: function () {
        this.$router.push({
              name: 'Signup'
            })
      },

      goToFindPassword: function () {

      },

    }


  }
</script>

<style>

</style>