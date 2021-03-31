<template>
  <v-container>
    <v-row>
      <v-col class="d-flex justify-center mt-13">
        <h1>언어 선택 -> text입력 -> 재생 </h1>
      </v-col>
    </v-row>


    <v-row>
      <v-col>
        
         
         <select id="select-lang" style="background-color:pink">
            <option value="ko-KR">한국어</option>
            <option value="ja-JP" selected>일본어</option>
            <option value="en-US">영어</option>
          </select>
          <textarea id="text" rows="5" cols="20" style="background-color: beige"></textarea>
          <button id="btn-read" @click="letsgo" class="main-background-color">재생</button>
        
      </v-col>
    </v-row>


  </v-container>
</template>
<script>
  export default {

    name: 'TTSOnlyJS',
    
    methods: {
      speak(text, opt_prop) {
        if (typeof SpeechSynthesisUtterance === "undefined" || typeof window.speechSynthesis === "undefined") {
          alert("이 브라우저는 음성 합성을 지원하지 않습니다.")
          return
        }

        window.speechSynthesis.cancel() // 현재 읽고있다면 초기화

        const prop = opt_prop || {}

        const speechMsg = new SpeechSynthesisUtterance()
        speechMsg.rate = prop.rate || 1 // 속도: 0.1 ~ 10      
        speechMsg.pitch = prop.pitch || 1 // 음높이: 0 ~ 2
        speechMsg.lang = prop.lang || "ko-KR"
        speechMsg.text = text

        // SpeechSynthesisUtterance에 저장된 내용을 바탕으로 음성합성 실행
        window.speechSynthesis.speak(speechMsg)
      },

      letsgo() {
        const selectLang = document.getElementById("select-lang")
        const text = document.getElementById("text")
        // const btnRead = document.getElementById("btn-read")

        this.speak(text.value, {
          rate: 1,
          pitch: 1.2,
          lang: selectLang.options[selectLang.selectedIndex].value
        })

      }
    }
  }
</script>
  <style scoped>
   
  </style>