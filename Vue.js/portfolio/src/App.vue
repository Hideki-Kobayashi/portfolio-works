<template>
  <div class="container">
    <div class="container__header">
      <div class="header">
        <div class="header__left">
          東京、フリーエンジニア 小林秀樹
        </div>
        <div class="header__right"></div>
      </div>
    </div>

    <div class="body__nav nav">
      <div class="nav-top-item">
        <img class="nav-img" src="./assets/img/my-img.jpg">
        <div class="nav-catch">
          Engineer<br>
          Hideki Kobayashi
        </div>
      </div>
      <div class="nav-bottom-items">
        <router-link to="/" class="nav-item">HOME</router-link>
        <router-link to="/Portfolio" class="nav-item">PORTFOLIO</router-link>
        <router-link to="/Biography" class="nav-item">BIOGRAPHY</router-link>
        <router-link to="/Contact" class="nav-item">CONTACT</router-link>
        <router-link to="/Information" class="nav-item" style="display: none;">INFORMATION</router-link>
      </div>

    </div>

    <div class="body__main-section main-section">
      <router-view />
    </div>

    <div class="container__footer">
      <div class="footer">
        <div class="footer__text">
          &copy; Hideki Kobayashi
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'App'
  }

</script>

<style lang="scss">
  
/*-----------------------------------
*  default stylesheet
*-----------------------------------*/
  * {
    box-sizing: border-box;
  }

  html {
    font-size: 62.5%;
  }

  body {
    font-size: 1.6rem;
    color: #323232;
  }

  a {
    display: inline;
    color: inherit;
    text-decoration: none;
  }

  img {
    display: block;
    width: 100%;
    height: auto;
  }


/*-----------------------------------
*  main stylesheet
*-----------------------------------*/

  .container {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    width: 100%;
    height: 100vh;

    display: grid;
    grid-template:
      "header header"4rem "nav main"calc(100vh - 8rem) "footer footer"
      /25rem 1fr;

    &__header {
      width: 100%;
      height: 4rem;
      grid-area: header;
    }

    &__footer {
      width: 100%;
      height: 4rem;
      grid-area: footer;
    }
  }


/*-----------------------------------
*  header stylesheet
*-----------------------------------*/

  .header {
    width: 100%;
    height: 4rem;
    color: white;
    background-color: black;
    display: flex;
    align-items: center;

    &__left {
      margin-left: 2rem;
    }
  }

/*-----------------------------------
*  body stylesheet
*-----------------------------------*/

  //body style
  .body {
    height: calc(100vh - 8rem);
    display: flex;
    overflow: hidden;

    &__nav {
      width: 100%;
    }

    &__main-section {
      height: 100%;
      grid-area: main;
    }
  }

  //nav style
  .nav {
    width: 25rem;
    height: 100%;
    padding-top: 3rem;
    color: white;
    background-color: black;
    font-size: 1.6rem;
    grid-area: nav;

    &-top-item {
      text-align: center;
    }

    &-bottom-items {
      margin-top: 5rem;
      text-align: center;
    }

    &-img {
      width: 60%;
      margin: auto;
    }

    &-item {
      margin-top: 1rem;
      display: block;
    }
  }

  //main-section style
  .main-section {
    width: 100%;
    height: 100%;

    overflow: scroll;
  }


/*-----------------------------------
*  footer stylesheet
*-----------------------------------*/

  .footer {
    width: 100%;
    height: 100%;
    color: white;
    background-color: black;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
  }

</style>
