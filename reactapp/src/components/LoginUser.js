import React, {useEffect, useState} from "react";
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

export default function LoginUser(){
    const [email, setEmial] = useState([]);
    const [password, setPassword] = useState([]);
    const [message, setMessage] = useState("");
    const API = 'http://127.0.0.1:8000/login';
    let handleSubmit = async (e) => {
        e.preventDefault();
        try{
            let response = axios({
                method: "POST",
                url: 'http://127.0.0.1:8000/login',
                mode : "same-origin",
                credentials: "include",
                headers: {
                    'Access-Control-Allow-Credentials': true,
                    'Access-Control-Allow-Headers': 'accept, accept-encoding, authorization, content-type, dnt, origin, user-agent, x-csrftoken, x-requested-with',
                    'Access-Control-Allow-Origin': 'http://127.0.0.1:3000',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'

                },
                withCredentials:true,
                body: JSON.stringify({
                    email: email,
                    password: password
                }),
            })
            if (response.status == 200){
                setEmial("");
                setPassword("")
                setMessage("U are log in");
                console.log(response.user);
            }
            else{
                console.log("HTTP REsponse different than 200");
                console.log(email);
                console.log(password);
            }
        }catch (err){
            console.log(err);
        }
    }
    return (
        <div>
            <form onSubmit={handleSubmit} method="post">
                <input
                    type="text"
                    value={email}
                    placeholder="Email"
                    onChange={(e) => setEmial(e.target.value)}
                />
                <input
                    type="text"
                    value={password}
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
                {message}
            </form>
        </div>
    );
}