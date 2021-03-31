<template>
 
  <div class="mypage_body">
    <v-container>
      <v-row>
        <v-col cols="6">
          <v-avatar size="150" class="my_avatar">
            <img
              src="@/assets/img/mypage/man.png"
            >
          </v-avatar>
          
        </v-col>
        <v-col cols="6">
          <div class="my_info">
            <p>test1</p>
            <v-btn
              icon
              class="my_info_icon"
            >
              <v-icon>mdi-cog-outline</v-icon>
            </v-btn>
            <br>
            <p>test1@test1.com</p>

          </div>

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
      
    </div>

    <v-row class="delete_icon">
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
    </v-row>

    
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

.my_info_icon {
  margin-left: 40%;
  margin-bottom: 3%;
}

.mypage_body {
  background-color: whitesmoke;
  height: 100%;
  width: 100%;
}

.my_avatar {
  margin-top: 5%;
  margin-left: 3%;
  margin-bottom: 10%;
}

.three_items {
  margin-bottom: 3%;
}

.three_icons {
  margin-right: 0.1%;  
}

.title_row {
  justify-content: space-between;
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