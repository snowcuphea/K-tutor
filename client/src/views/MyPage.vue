<template>
  <div>
    <div class="page-modal-overlay"
      v-if="visible"
      @click="closeModal"
      >
      <div class="page-modal-window">

        <v-carousel :show-arrows="false" hide-delimiters>
          <v-carousel-item
            v-for="(it,i) in item.src"
            :key="i"
          >
            <v-img :src="it" class="page_img"></v-img>
          </v-carousel-item>
        </v-carousel>
      </div>

    </div>
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

          <appMyPageDetail :pageDetailItem="item" @pageUpdate="pageDetail" />

        </v-list>
        <div @click="ask">
          <v-list style="padding-left: 16px; padding-top: 16px; padding-bottom: 16px; margin-bottom: 5%;">
            문의하기
          </v-list>

        </div>
        <div
          class="page-modal-overlay"
          v-if="askVisible"
        >
          <v-btn
            style ="top: -45%; right: -10px;"
          >
            <v-icon @click="closeAsk">mdi-close</v-icon>
          </v-btn>
          <v-card style="width:80%;">
            <div class="ask-modal-window">
              
              <v-text-field
                label="name"            
                placeholder="please enter your name"
              ></v-text-field>
              <v-text-field
                label="email"            
                placeholder="please enter your eamil ex) asd@asd.com"
              ></v-text-field>
              <v-textarea
                label="contents"            
                placeholder="Please fill out your inquiry"
              ></v-textarea>
              <v-btn
                class="mr-4"
                @click="submit"
              >
                submit
              </v-btn>
              <v-btn @click="clear">
                clear
              </v-btn>
            </div>

          </v-card>

            

        </div>

      </div>

      <v-row class="delete_icon">
        <v-col cols="4">
          <v-btn color="red">
            Delete
          </v-btn>
        </v-col>
        <v-col class="logout_icon" cols="4">
          <v-btn color="red lighten-2">
            Logout
          </v-btn>
        </v-col>
      </v-row>

    </div>
  </div>
</template>

<script>
import MyPageDetail from '../components/mypage/MyPageDetail'

export default {
  components: {
    appMyPageDetail: MyPageDetail
  },
  data: () => ({
    myPageItems: [
      {
        title: 'Tutorial',
        src: [require('@/assets/img/mypage/1.png'), require('@/assets/img/mypage/2.png'), require('@/assets/img/mypage/3.png'), require('@/assets/img/mypage/4.png'), require('@/assets/img/mypage/5.png')],
        contents: '',
      },
      {
        title: '공지사항',
        contents: '공지사항 내용',
      },
      {
        title: '문의하기',
        contents: 'ssafy로 ㄱㄱ',
      },
      // {
      //   title: '이용약관',
      //   contents: '??',
      // },
      {
        title: '오픈소스 정보',
        contents: '',
      },
    ],
    visible: false,
    askVisible: false,
   
  }),
  methods: {
    pageDetail (pageDetailItem) {
      this.item = pageDetailItem
      this.visible = !this.visible
    },
    closeModal () {
      this.visible = !this.visible
    },
    ask () {
      this.askVisible = !this.askVisible
    },
    closeAsk () {
      this.askVisible = !this.askVisible
    },
    
  },
 

}
</script>

<style>

.page-modal-overlay {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

.page-modal-window {
  width: 80%;
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

</style>