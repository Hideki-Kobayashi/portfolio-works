<template>
  <div class="contact">
    <div class="contact__header">
      <div class="header-catch">Contact</div>
    </div>

    <div class="contact__content con-content">
      <div>※Google Formの読み込みに時間がかかる場合があります。</div>

      <div class="form">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdyhyjQoItcthUmIMPlJWc60uATTTs4K3AKltj2FCRx68N9QA/viewform?embedded=true" width="640" height="1242" frameborder="0" marginheight="0" marginwidth="0">読み込んでいます...</iframe>
      </div>

      <div class="form-sp">
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdyhyjQoItcthUmIMPlJWc60uATTTs4K3AKltj2FCRx68N9QA/viewform?embedded=true" width="288" height="1242" frameborder="0" marginheight="0" marginwidth="0">読み込んでいます...</iframe>
      </div>
    </div>
  </div>
</template>


<style lang="scss">
  $sp: 768px; // スマホなど

  @mixin sp {
    @media (max-width: ($sp)) {
      @content;
    }
  }

  .header-catch {
    font-size: 3rem;
    padding-top: 2rem;
    padding-left: 2rem;
  }

  .contact__content {
    width: 80%;
    margin: auto;
    margin-top: 5rem;
    @include sp{
      width: 90%;
    }
  }

  .con-content {
    font-size: 1.6rem;
    padding-top: 2rem;
  }
  
  .form {
    @include sp {
      display: none;
    }
  }

  .form-sp {
    display: none;

    @include sp {
      display: block;
    }
  }

</style>
