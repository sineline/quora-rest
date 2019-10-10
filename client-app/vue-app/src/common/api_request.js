class APIRequest {
    data = {};
    token = localStorage.token; // Global Token - From Login
    header = {};
    request_init = {};
    response_status = 0;

    constructor(url, method = "GET", body_request = {}){
        this.url = url;
        this.method = method;
        this.body_request = body_request;

        this.set_header();
        this.set_request_init();
    }

    async call_api(){
        const response = await fetch(this.url, this.request_init);
        this.response_status = await response.status;

        if(this.method == "DELETE" && this.response_status.toString().charAt(0) == "2")
            return this.data =  JSON.stringify({message:"Correctly deleted"});

        return this.data = await response.json();
    }

    set_request_init(){
        this.request_init['method'] = this.method;
        this.request_init['headers'] = this.header;
        if(Object.keys(this.body_request).length)
            this.request_init['body'] = JSON.stringify(this.body_request);
    }

    set_header(){
        if(this.token)
            this.header['Authorization'] = 'Token '+this.token;

        if(this.method == "PUT" || this.method == "POST")
            this.header['Content-Type'] = 'application/json';
    }

    set_url(url){
        this.url = url;
    }

    set_method(method){
        this.method = method;
    }

    get_data(){
        return this.data;
    }

    get_response_status(){
        return this.response_status;
    }
}

export default APIRequest;