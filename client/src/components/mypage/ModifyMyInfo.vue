<template>
  <div>
    <v-dialog
      v-model="showModifyMyInfo"
      fullscreen
    >
      <v-card width="100%" height="100%" tile>

        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Information </h2>
            <v-btn
                icon
                class="close-dialog"
                @click="hideDialog"
            >
                <v-icon>mdi-close</v-icon>
            </v-btn>

        <v-form ref="form" lazy-validation>
            <v-row style="height:60vh" class="d-flex align-center">
                <v-col>

                    <v-row class="mx-5 d-flex align-center">
                        <v-col
                            cols="4"
                            style="padding-bottom: 0"
                        >
                            <h4>
                                Nickname:   
                            </h4>
                        </v-col>
                        <v-col>
                            <v-text-field label="Nickname" :rules="rulesNickname" hide-details="auto"
                                v-model="this.$store.state.nickName"></v-text-field>
                        </v-col>
                        
                    </v-row>
                    <v-row class="mx-5 d-flex align-center">
                        <v-col
                            cols="4"
                            style="padding-bottom: 0"
                        >
                            <h4>
                                Password:   
                            </h4>
                        </v-col>
                        <v-col>
                            <v-text-field label="Password" :rules="rulesNickname" hide-details="auto" type="password"
                                v-model="this.$store.state.nickName"></v-text-field>
                        </v-col>
                        
                    </v-row>
                    <v-row class="mx-5 d-flex align-center">
                        <v-col
                            cols="4"
                            style="padding-bottom: 0"
                        >
                            <h4>
                                Password Confirm:   
                            </h4>
                        </v-col>
                        <v-col>
                            <v-text-field label="Password Confirm" :rules="rulesNickname" hide-details="auto" type="password"
                                v-model="this.$store.state.nickName"></v-text-field>
                        </v-col>
                        
                    </v-row>
                    <v-row>
                        <v-col class="d-flex justify-end mr-7">
                            <v-btn @click="modify">Modify</v-btn>
                        </v-col>
                    </v-row>


                </v-col>
            </v-row>
        </v-form>


      </v-card>
      
    </v-dialog>
  </div>

</template>

<script>
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
      signupCredentials: {
          userNickname: "",
      }

  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    },
    // modify() {
    //     if ()
    // }
    
    },

}
</script>

<style>

</style>