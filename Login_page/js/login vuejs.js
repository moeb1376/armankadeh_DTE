
var loginform = new Vue({
    el: "#Login",
    data: {
        password : '',
        passwordFieldType : 'password',
        "seen": true
    },
    methods: {
        change_pages: function () {
            loginform.seen = false;
            signupform.show = true

        },
        show_hide_pass: function () {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
        },
        hide_pass:function () {
            this.passwordFieldType = 'password'
        }
    }

})

var signupform = new Vue({
    el: "#SignUp",
    data: {
        password : '',
        re_password:'',
        passwordFieldType : 'password',
        repasswordFieldType : 'password',
        "show": false
    },
    methods: {
        change_pages1: function () {
            loginform.seen = true;
            signupform.show = false

        },
        show_hide_pass: function () {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
        },
        hide_pass:function () {
            this.passwordFieldType = 'password'
        },
        show_hide_repass: function () {
            this.repasswordFieldType = this.repasswordFieldType === 'password' ? 'text' : 'password'
        },
        hide_repass:function () {
            this.repasswordFieldType = 'password'
        }

    }
})
// const passwordField = document.querySelector('#password')
//
// function switchVisibility() {
//     if (passwordField.getAttribute('type') === 'password') passwordField.setAttribute('type','text')
//     else passwordField.setAttribute('type', 'password')
//
// }
