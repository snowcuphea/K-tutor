<template>
  <div>

    <v-dialog v-model="showDeleteAccount">
      <v-card>
        <v-card-title class="headline d-flex justify-center" style="padding: 12px; background-color: white;"> Delete Account </v-card-title>
        <v-card-text style="margin:0">If you delete your account, you can't use the service.</v-card-text>
        <v-card-text style="margin:0">Are you sure you want to delete your account?</v-card-text>
        <v-card-actions class="d-flex justify-space-between">
        <v-btn text color="red" @click="deleteAccountReally">
          Delete
        </v-btn>

        <v-btn text color="black"  @click="hideDialog">
          Cancel
        </v-btn>

</v-card-actions>
      </v-card>

    </v-dialog>
  </div>
</template>

<script>
import {
    deleteUser
  } from "@/api/account.js"


  export default {
    props: ['showDeleteAccount'],
    data: () => ({

    }),
    methods: {
      hideDialog() {
        this.$emit('hideTutorial')
      },

      deleteAccountReally(){
        deleteUser(
          (res) => {
            console.log("deleteAccount(),", res)
            this.$store.dispatch('deleteUser')
              .then(() => {
                this.$emit('hideTutorial')
                alert("ByeBye...")
                this.$router.push({
                  name: 'Login'
                })
              })
              .catch(() => {})
          },
          (err) => {
            console.log("deleteAccount(),", err)
          }
        )


      }
    }
  }
</script>

<style>

</style>