<template>
  <v-container>
    <v-dialog
      v-model="showOpenSource"
      fullscreen
    >
      <v-card>
        <h2 class="head d-flex justify-center" style="padding: 12px; background-color: white;"> OpenSource </h2>
          <v-btn
            icon
            class="close-dialog"
            @click="hideDialog"
          >
            <v-icon>mdi-close</v-icon>
        </v-btn>
          <v-list
            v-for="(item,idx) in openSourceItems"
            :key = "idx"
          >
            <div class="openSource_all">
              <h1>{{ item.name }}</h1>
              <div class="openSource_contents">
                <h4>{{ item.version }}</h4>
                <a :href="item.url"><h5>{{ item.url }}</h5></a>
                <h5>{{ item.copyright }}</h5>

              </div>

            </div>

          </v-list>

      </v-card>

    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: ['showOpenSource'],
  data: () => ({
    openSourceItems: [
      {
        name: 'Python',
        version: '3.7.7',
        url: 'https://www.python.org/',
        copyright: 'Copyright © 2001-2021 Python Software Foundation; All Rights Reserved',
      },
      {
        name: 'Django',
        version: '3.1.1',
        url: 'https://www.djangoproject.com/',
        copyright: 'Copyright Django Software Foundation; All Rights Reserved',
      },
      {
        name: 'MariaDB',
        version: '-',
        url: 'https://mariadb.org/',
        copyright: 'Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others',
      },
      {
        name: 'AWS',
        version: '-',
        url: 'https://aws.amazon.com/',
        copyright: 'Effective Date – April 18, 2008 © 2008 Amazon.com, Inc. or its affiliates. All rights reserved',
      },
      {
        name: 'Pandas',
        version: '0.25.3',
        url: 'https://pandas.pydata.org/',
        copyright: 'Copyright (c) 2011-2020, Open source contributors',
      },
      {
        name: 'KoNLPy',
        version: '0.5.2',
        url: 'https://konlpy.org/',
        copyright: '© Copyright 2014-2019, KoNLPy (GPL license)',
      },
      {
        name: 'Gensim',
        version: '3.8.3',
        url: 'https://radimrehurek.com/gensim/',
        copyright: '© Copyright 2009-now, Radim Řehůřek. Last updated on Mar 25, 2021',
      },
      {
        name: 'google-trans-new',
        version: '1.1.9',
        url: 'https://pypi.org/project/google-trans-new/',
        copyright: 'Copyright (c) 2020 lushan88a, licensed under the MIT License',
      },
      {
        name: 'Vuex',
        version: '3.4.0',
        url: 'https://vuex.vuejs.org/',
        copyright: 'Copyright (c) 2015-present Evan You, licensed under the MIT License',
      },
      {
        name: 'Vue-Router',
        version: '3.2.0',
        url: 'https://router.vuejs.org/',
        copyright: 'Copyright (c) 2013-present Evan You, licensed under the MIT License',
      },
      {
        name: 'Vuetify',
        version: '2.4.0',
        url: 'https://vuetifyjs.com/',
        copyright: 'Copyright (c) 2016-present Vuetify LLC, licensed under the MIT License',
      },
      {
        name: 'Chart.js',
        version: '2.9.4',
        url: 'https://www.chartjs.org/',
        copyright: 'Copyright © 2018 Chart.js Contributors, licensed under the MIT License',
      },
      // {
      //   name: 'google-trans-new',
      //   version: '-',
      //   url: 'https://pypi.org/project/google-trans-new/',
      //   copyright: 'Copyright (c) 2020 lushan88a, licensed under the MIT License',
      // },


      
    ]
  }),
  methods: {
    hideDialog () {
      this.$emit('hideTutorial')
    }
  }
}
</script>

<style>

.openSource_all {
  margin-left: 5%;
}

.openSource_contents {
  margin-left: 5%;
}

</style>