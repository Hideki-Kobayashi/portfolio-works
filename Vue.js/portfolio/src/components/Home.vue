<template>
  <div class="home">
    <div class="home__header">
      <div class="header-catch">Home</div>
    </div>

    <div class="home__main-catch">
      小林秀樹の<br class="br-sp">
      ポートフォリオ
    </div>
  </div>
</template>

<style lang="scss" scoped>
  $sp: 768px; // スマホなど

  @mixin sp {
    @media (max-width: ($sp)) {
      @content;
    }
  }

  .home {
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/home-bg.jpg);
    position: relative;
  }

  .header-catch {
    font-size: 3rem;
    color: white;
    padding-top: 2rem;
    padding-left: 2rem;

  }

  .home__main-catch {
    color: white;
    font-size: 2.4rem;
    position: absolute;
    top: 16rem;
    right: 8rem;

    @include sp {
      font-size: 2.4rem;
    }
  }

  .br-sp {
    display: none;

    @include sp {
      display: block;
    }
  }

</style>
