<template>
  <v-container>
    <v-dialog
      v-model="showInquiry"
      fullscreen
    >
      <v-card style="position: fixed;">

        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> Inquiry </h2>
          <v-btn
            icon
            class="close-dialog"
            @click="hideDialog"
          >
            <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-form
          ref="form" 
          lazy-validation
          style="background-color: white; margin-top:10%; margin-left: 10%;"
          >
          <v-row
            style="height:60vh"
            class="d-flex align-center"
          >
            <v-col>
              <v-row>
                <v-col>
                  <v-text-field
                    label="name"            
                    placeholder="please enter your name"
                    style="width:80%;"
                  ></v-text-field>

                </v-col>

              </v-row>
              <v-row>
                <v-col>
                  <v-text-field
                    :rules="rulesEmail"
                    label="email"            
                    placeholder="please enter your eamil ex) asd@asd.com"
                    style="width:80%;"
                  ></v-text-field>

                </v-col>

              </v-row>
              <v-row>
                <v-col>
                  <v-textarea
                    label="contents"            
                    placeholder="Please fill out your inquiry"
                    style="width:80%;"             
                  ></v-textarea>

                </v-col>

              </v-row>

            </v-col>
          
          </v-row>
          <v-row class="send_icons" style="margin-right: 30%;">
            <v-btn
            >
              Send
            </v-btn>
            
          </v-row>
        </v-form> 
      </v-card>

    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: ['showInquiry'],
  data: () => ({
    rulesEmail: [
      value => !!value || 'Required.',
      value => /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/.test(value) ||
      'Confirm your Email.',
    ],
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  }
}
</script>

<style>

</style>