<template>

  <div class="mypage_body">
    <v-container>
      <v-row>
        <v-col cols="5">
          <div>
            <v-avatar size="100" class="my_avatar">
              <img :src="myImgSource()">
            </v-avatar>
          </div>

        </v-col>
        <v-col cols="7" class="d-flex align-center">
          <v-row class="d-flex flex-column">
            <div class="d-flex align-center">

              <h4>{{ $store.state.nickName }}</h4>
              <v-btn icon class="my_info_icon">
                <v-icon @click="showDialog('ModifyMyInfo')">mdi-cog-outline</v-icon>
              </v-btn>
            </div>

            <h4>{{ $store.state.userEmail }}</h4>


          </v-row>

        </v-col>
      </v-row>
    </v-container>

    <div class="pb-10">

      <v-list v-for="(item, idx) in myPageItems" :key="idx">
        <v-list-item @click="showDialog(item)">
          {{ item.title }}
        </v-list-item>

      </v-list>
      <v-list-item style="background: white" @click="logout">
        Logout
      </v-list-item>
      <span style="color: blue;" class="d-flex justify-center" @click="showDialog({title: 'DeleteAccount'})">Delete Account</span>

    </div>

  
  <Tutorial :showTutorial="showTutorial" @hideTutorial="showTutorial = !showTutorial"/>
  <Notice :showNotice="showNotice" @hideTutorial="showNotice = !showNotice"/>
  <Inquiry :showInquiry="showInquiry" @hideTutorial="showInquiry = !showInquiry"/>
  <TermsOfUse :showTermsOfUse="showTermsOfUse" @hideTutorial="showTermsOfUse = !showTermsOfUse"/>
  <OpenSource :showOpenSource="showOpenSource" @hideTutorial="showOpenSource = !showOpenSource"/>
  <DeleteAccount :showDeleteAccount="showDeleteAccount" @hideTutorial="showDeleteAccount = !showDeleteAccount"/>
  <ModifyMyInfo :showModifyMyInfo="showModifyMyInfo" @hideTutorial="showModifyMyInfo = !showModifyMyInfo"/>
  </div>

</template>

<script>
  import { mapState } from 'vuex'

  import Tutorial from '../components/mypage/Tutorial'
  import Notice from '../components/mypage/Notice'
  import Inquiry from '../components/mypage/Inquiry'
  import TermsOfUse from '../components/mypage/TermsOfUse'
  import OpenSource from '../components/mypage/OpenSource'
  import DeleteAccount from '../components/mypage/DeleteAccount'
  import ModifyMyInfo from '../components/mypage/ModifyMyInfo'
  
  export default {
    components: {
      Tutorial,
      Notice,
      Inquiry,
      TermsOfUse,
      OpenSource,
      DeleteAccount,
      ModifyMyInfo,

    },
    data: () => ({
      nowTime: new Date(),
      myPageItems: [{
          title: 'Tutorial',
        },
        {
          title: 'Notice',
        },
        {
          title: 'Inquiry',
        },
        {
          title: 'TermsOfUse',
        },
        {
          title: 'OpenSource',
        },
         
      ],
      visible: false,
      showTutorial: false,
      showNotice: false,
      showInquiry: false,
      showTermsOfUse: false,
      showOpenSource: false,
      showDeleteAccount: false,
      showModifyMyInfo: false,
      tempLevel: 15,
    }),
    methods: {
      pageDetail(pageDetailItem) {
        this.item = pageDetailItem
        this.visible = !this.visible
      },
      closeModal() {
        this.visible = !this.visible
      },
      showDialog(item) { 
        if (item.title == 'Tutorial') {
          this.showTutorial = !this.showTutorial
        } else if (item.title == 'Notice') {
          this.showNotice = !this.showNotice
        } else if (item.title == 'Inquiry') {
          this.showInquiry = !this.showInquiry
        } else if (item.title == 'TermsOfUse') {
          this.showTermsOfUse = !this.showTermsOfUse
        } else if (item.title == 'DeleteAccount'){
          this.showDeleteAccount = !this.showDeleteAccount
        } else if (item == 'ModifyMyInfo') {
          this.showModifyMyInfo = !this.showModifyMyInfo
        } else {
          this.showOpenSource = !this.showOpenSource
        }
      },
      myImgSource() {
        if (this.tempLevel > 14) {
          return require('@/assets/img/mypage/sejong-the-great.png')
        } else if (this.tempLevel > 11) {
          return require('@/assets/img/mypage/korea.png')
        } else if (this.tempLevel > 8) {
          return require('@/assets/img/mypage/empress.png')
        } else if (this.tempLevel > 5) {
          return require('@/assets/img/mypage/emperor.png')
        } else if (this.tempLevel > 2) {
          return require('@/assets/img/mypage/woman.png')
        } else {
          return require('@/assets/img/mypage/man.png')
        }
      },
      logout() {
        this.$store.dispatch("logout")
          .then(() => {
            // alert("You have been logged out.")
            const alertInfo = {
              status: true,
              color: "success",
              content: "You have been logged out."
            }
            this.$store.dispatch("showAlert", alertInfo)
            this.$router.push({
              name: 'Login'
            })
          })
          .catch(() => {})

      },

     
    },
    created() {
      // console.log(this.time, this.nowTime.getDate())
      if ( this.nowTime.getDate() !== this.time ) {
        console.log(this.time, this.nowTime.getDate())
        this.$store.dispatch( 'resetChance', this.nowTime.getDate() )
      } 

    },
    computed: {
      ...mapState(["time"])
    }


  }
</script>

<style>
  .page-modal-overlay {
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: white;
  }


  .page_img {
    height: 100%;
    width: 100%;
  }

  .ask-modal-window {
    background-color: white;
    z-index: 3;
    width: 100%;
    margin-right: 30px;
  }

  .my_info {
    margin-top: 30%;
  }

  .mypage_body {
    background-color: white;
    height: 100%;
    width: 100%;
  }

  .my_avatar {
    margin-top: 5%;
    margin-left: 3%;
    margin-bottom: 10%;
  }

  .title_list {
    margin-left: 5%;
    margin-top: 4.5%;
    margin-bottom: 3%;
    font-size: 120%;
    font-weight: bolder;
  }

  .title_btn {
    margin-top: 3%;
    margin-right: 5%;
  }

  .delete_icon {
    justify-content: space-around;
  }

  .send_icons {
    justify-content: flex-end;
    margin-right: 10%;
  }
</style>