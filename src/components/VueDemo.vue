<template>
  <div id="character-target-div"></div>
</template>

<script>

import HanziWriter from 'hanzi-writer';

export default {
  name: 'VueDemo',
  mounted() {
     HanziWriter.create('character-target-div', '我', {
      width: 100,
      height: 100,
      padding: 5
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

img {
  width: 250px;
}

</style>
