new Vue({
  el: "#app",
  data: {
    users: [],
    posts: [],
    post: ''
  },
  methods: {
    Showpost(id, i) {
      fetch("https://jsonplaceholder.typicode.com/posts?userId=" + id)
        .then(response => response.json())
        .then((data) => {
          this.post = data[i];

        })
    },
  },
  mounted() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(response => response.json())
      .then((data) => {
        this.users = data;
      })
  },
  template: `
<div class="flex">

  <div v-for="user, i in users">
    <button class="btn" v-on:click="Showpost(user.id, i)" >{{ user.name }}</button>
  </div>
  <h1>{{ post.title }}</h1>
</div>
`,
});