import React, {useEffect, useState} from "react";
import axios from "axios";
import cors from "cors";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;
const client = axios.create({
    baseURL: "http://127.0.0.1:8000"
})
export default function LoginUser(){
    const [email, setEmial] = useState([]);
    const [password, setPassword] = useState([]);
    const [message, setMessage] = useState("");
    const API = 'http://localhost:8000/login';
    let handleSubmit = async (e) => {
        e.preventDefault();
        try{
            let response = client.post(API,{
                    email:email,
                    password:password
                }
            )
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
                console.log(response)
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