import React, {useEffect, useState} from "react";
export default function Users(){
    const [user, getUser] = useState([]);
    const API = 'http://127.0.0.1:8000/api/users/';
    const fetchUsers = () => {
        fetch(API)
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                getUser(res);
            })
    }
    useEffect(() => {
        fetchUsers()
    },[])
    return (
        <div>
            <ul>
                {user.map((item, i) => {
                    return <li>{item.name}</li>
                })}
            </ul>
        </div>
    )
}

