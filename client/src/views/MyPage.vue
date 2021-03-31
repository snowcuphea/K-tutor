<template>
 
  <div class="mypage_body">
    <v-container>
      <v-row>
        <v-col cols="6">
          <div>
            <v-avatar size="150" class="my_avatar">
              <img
                :src="myImgSource()"
              >
            </v-avatar>
          </div>
          
        </v-col>
        <v-col cols="6" class="d-flex align-center">
          <v-row class="d-flex flex-column">
            <div class="d-flex align-center">

              <h4>{{ $store.state.nickName }}</h4>
              <v-btn icon class="my_info_icon">
                <v-icon>mdi-cog-outline</v-icon>
              </v-btn>
            </div>
            
            <h4>{{ $store.state.userEmail }}</h4>


          </v-row>


          <!-- <div class="my_info">
          </div> -->

        </v-col>
      </v-row>
    </v-container>

    <div>
              
      <v-list
        v-for = "(item, idx) in myPageItems"
        :key = "idx"
        
      >
        <v-list-item
          @click="showDialog(item)"
        >
          {{ item.title }}
        </v-list-item>

      </v-list>
      <v-list-item style="background: white" @click="logout">
        Logout
      </v-list-item>
      <a href="" class="d-flex justify-center">Delete Account</a>
      
    </div>

    <!-- <v-row class="delete_icon">
      <v-col cols="4">
        <v-btn color="red">
          Delete
        </v-btn>
      </v-col>
      <v-col class="logout_icon" cols="4">
        <v-btn color="red lighten-2" @click="logout">
          Logout
        </v-btn>
      </v-col>
    </v-row> -->

    

  <Tutorial :showTutorial="showTutorial" @hideTutorial="showTutorial = !showTutorial"/>
  <Notice :showNotice="showNotice" @hideTutorial="showNotice = !showNotice"/>
  <Inquiry :showInquiry="showInquiry" @hideTutorial="showInquiry = !showInquiry"/>
  <TermsOfUse :showTermsOfUse="showTermsOfUse" @hideTutorial="showTermsOfUse = !showTermsOfUse"/>
  <OpenSource :showOpenSource="showOpenSource" @hideTutorial="showOpenSource = !showOpenSource"/>
  </div>
  
</template>

<script>
import Tutorial from '../components/mypage/Tutorial'
import Notice from '../components/mypage/Notice'
import Inquiry from '../components/mypage/Inquiry'
import TermsOfUse from '../components/mypage/TermsOfUse'
import OpenSource from '../components/mypage/OpenSource'

export default {
  components: {
    Tutorial,
    Notice,
    Inquiry,
    TermsOfUse,
    OpenSource

  },
  data: () => ({
    myPageItems: [
      {
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
    tempLevel: 15,
  }),
  methods: {
    pageDetail (pageDetailItem) {
      this.item = pageDetailItem
      this.visible = !this.visible
    },
    closeModal () {
      this.visible = !this.visible
    },
    showDialog (item) {
      if (item.title == 'Tutorial') {
        this.showTutorial = !this.showTutorial
      }
      else if (item.title == 'Notice') {
        this.showNotice = !this.showNotice
      }
      else if (item.title == 'Inquiry') {
        this.showInquiry = !this.showInquiry
      }
      else if (item.title == 'TermsOfUse') {
        this.showTermsOfUse = !this.showTermsOfUse
      }
      else {
        this.showOpenSource = !this.showOpenSource
      }
    },
    myImgSource () {
      if (this.tempLevel > 14) {
        return require('@/assets/img/mypage/sejong-the-great.png')
      }
      else if (this.tempLevel > 11) {
        return require('@/assets/img/mypage/korea.png')
      }
      else if (this.tempLevel > 8) {
        return require('@/assets/img/mypage/empress.png')
      }
      else if (this.tempLevel > 5) {
        return require('@/assets/img/mypage/emperor.png')
      }
      else if (this.tempLevel > 2) {
        return require('@/assets/img/mypage/woman.png')
      }
      else {
        return require('@/assets/img/mypage/man.png')
      }},
    logout(){
      this.$store.dispatch("logout")
      .then( ()=>{
        alert("You have been logged out.")
     
        this.$router.push({
          name: 'Login'
        })

      })
      .catch( () => {
      
      })
      
    }

  
  },
 

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