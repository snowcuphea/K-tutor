<template>
  <div class="mypage_body">
    <div>
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
              <v-text>test1</v-text>
              <v-btn
                icon
                class="my_info_icon"
              >
                <v-icon>mdi-cog-outline</v-icon>
              </v-btn>
              <br>
              <v-text>test1@test1.com</v-text>

            </div>

          </v-col>
        </v-row>
      </v-container>

      <!-- <v-container class="three_items">
        <v-row class="three_icons">
          <v-col
            cols="4"
          >
            <v-card>
              <v-card-title>하이</v-card-title>
            </v-card>
          </v-col>
          <v-col
            cols="4"
          >
            <v-card>
              <v-card-title>하이</v-card-title>
            </v-card>
          </v-col>
          <v-col
            cols="4"
          >
            <v-card>
              <v-card-title>하이</v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container> -->


      <div>
        <v-list two-line>
          <v-list-item-group
            v-for="(item, idx) in items"
            :key="idx"
          >
            <appMyPage :pageModalItem="item" @pageUpdate="pageModal" />

            <v-card-actions>

              <v-row class="title_row">
                <div class="title_list">
                  {{ item.title }}
                </div>
                  <v-btn
                    icon
                    @click="show = !show"
                    class="title_btn"
                  >
                    <v-icon>{{ show ? 'mdi-chevron-left' : 'mdi-chevron-right' }}</v-icon>
                  </v-btn>

              </v-row>
            </v-card-actions>
            <v-expand-transition>
              <div v-show="show">
                <v-divider></v-divider>

                {{ item.contents }}                  

              </div>
            </v-expand-transition>


          </v-list-item-group>
                  
        
          <!-- <v-list-item-group
            v-for="(item, idx) in items"
            :key="idx"
          >
            <v-row class="title_row">
              <div class="title_list">
                {{ item.title }}
              </div>
              <v-btn
                icon
                @click="show = !show"
                class="title_btn"
              >
              <v-icon>{{ show ? 'mdi-chevron-left' : 'mdi-chevron-right' }}</v-icon>
            </v-btn>

            </v-row>
          </v-list-item-group> -->
        </v-list><br>

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
import Mypage from '../components/mypage/Mypage'

export default {
  components: {
    appMyPage: Mypage
  },
  data: () => ({
    items: [
      {
        title: 'Tutorial',
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
      {
        title: '이용약관',
        contents: '??',
      },
    ],
    show: false,
  }),
  methods: {
    pageModal (pageModalItem) {
      this.item = pageModalItem
    }
  }

}
</script>

<style>

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