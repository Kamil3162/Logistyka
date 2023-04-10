import React, {useEffect, useState} from "react";
export default function SamiTrucks(){
    const [samitrucks, getSamitrucks] = useState([]);
    const API = 'http://127.0.0.1:8000/api/samitrucks/';
    const fetchUsers = () => {
        fetch(API)
            .then((res) => res.json())
            .then((res) => {
                console.log(res);
                getSamitrucks(res);
            })
    }
    useEffect(() => {
        fetchUsers()
    },[])
    return (
        <div>
            trucks
            <ul>
                {samitrucks.map((item, i) => {
                    return <li>{item.brand}</li>
                })}
            </ul>
        </div>
    )
}