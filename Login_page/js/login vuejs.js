var global_data = new Vue({
    data: {
        seen: true,
        page_number: 1,
        relative_font_size: document.body.clientWidth
    }
});

var loginform = new Vue({
    el: "#Login",
    data: {
        password: '',
        passwordFieldType: 'password'
    },

    methods: {
        change_pages: function () {
            global_data.seen = false;
            // alert(document.body.clientWidth)
        },
        show_hide_pass: function () {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
        },
        new_pass_email: function () {
            loginform.display1 = true
        },
        return_global: function () {
            return global_data.seen;
        },
        return_global_size: function () {
            return global_data.relative_font_size
        }

    }
});

var signupform = new Vue({
    el: "#SignUp",
    data: {
        password: '',
        re_password: '',
        passwordFieldType: 'password',
        repasswordFieldType: 'password',
    },
    methods: {
        change_pages1: function () {
            global_data.seen = true;
        },
        show_hide_pass: function () {
            this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password'
        },
        show_hide_repass: function () {
            this.repasswordFieldType = this.repasswordFieldType === 'password' ? 'text' : 'password'
        },
        return_global: function () {
            return global_data.seen
        }
    }
});
