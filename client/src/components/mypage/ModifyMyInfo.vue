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
        <v-divider></v-divider>
        <!-- <v-row align="center">
            <v-col cols="2">
                <v-subheader>
                Month:
                </v-subheader>
            </v-col>

            <v-col cols="3">
                <v-select
                    v-model="select_month"
                    :items="items_month"
                    label="1"
                    persistent-hint
                    return-object
                    single-line
                >
                </v-select>
            </v-col>
            <v-col
                cols="2"
            >
                <v-subheader>
                    Days:
                </v-subheader>
            </v-col>
            <v-col cols="3">
                <v-select
                    v-model="select_day"
                    :items="items_day"
                    label="1"
                    persistent-hint
                    return-object
                    single-line
                >
                </v-select>
            </v-col>
            <v-col cols="2">
                <v-btn @click="search_name">ok</v-btn>
            </v-col>

        </v-row> -->


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
      },
    //   items_month: [
    //       1,2,3,4,5,6,7,8,9,10,11,12
    //   ],
    //   items_day: [
    //       1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
    //   ],
    //   select_month: '',
    //   select_day: '',
    //   select_name_month: [
    //       'Ssang', 'Chul', 'Bok', 'Dol', 'Pang', 'Yuk', 'Ssang', 'Gae', 'Chil', 'Gap', 'Sam', 'Bang'
    //   ]

  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    },
    // modify () {
    //     const form = []
    //     this.form.push({nickname: this.$store.state.nickName, password: ''})
    //     modify (
    //         this.form,
    //         (res) => {
    //             console.log(res)
    //         },
    //         (err) => {
    //             console.log('fail', err)
    //         }
    //     )
    // }

    
    // modify() {
    //     if ()
    // },
    // search_name () {
    //     if (this.select_month != '' && this.select_day != '') {
    //         if (this.select_month == 2) {

    //         }
    //         else if (this.select_month in [1,3,5,7,8,10,12]) {

    //         }
    //         else {

    //         }
    //     }
    // }
    },

}
</script>

<style>

</style>