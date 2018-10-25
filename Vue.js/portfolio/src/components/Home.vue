<template>
  <div class="home" style="background-image: url(../assets/img/home-bg.jpg);">
    <div class="home__header">
      <div class="header-catch">Home</div>
    </div>
    
    <div class="home__main-catch">
      小林秀樹のポートフォリオ
    </div>
  </div>
</template>

<style lang="scss" scoped>
  .home {
    width: 100%;
    height: 100%;
    
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
  }

</style>
