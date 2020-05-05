import React, { useState, useEffect } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './App.css';


function loadProductData(callback){
  // Product fetch via api with ajax
  let xhr = new XMLHttpRequest();
  let method = 'get';
  let pEndPoint = 'http://127.0.0.1:8000/api/product';
  // xhr.responseType = 'json'
  xhr.open(method, pEndPoint)
  console.dir(xhr)
  xhr.onload = function() {
      callback(xhr.response, xhr.status)
      // console.log(xhr.response)
  }
  xhr.send()
}

function App() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    function myCallBack(response, stauts) {
      // const prodictItems = [{'name': 'firest product'},{'name': 'second product'}]
      setProducts(JSON.parse(response))
    }
    loadProductData(myCallBack)
    
  }, []);

  return (
    <div className="App">
      <div>
        <div className="container">
          <div className="row">
            {products.map((obj, index) => {
              let imageUrl = obj.image != null ? obj.image : '/static/images/no_image_300x300.jpg'
              return (
                <div className="col-md-3 mt-4" key={index}>
                    <div className="card">
                        <img className="card-img-top" src={'http://127.0.0.1:8000' + imageUrl} alt={obj.name} />
                        <div className="card-body">
                            <h6 className="card-title">{obj.name}</h6>
                            <p className="card-text text-secondary" style={{minHeight:'24px'}}>{obj.content}</p>
                            <a className="btn btn-primary">Go somewhere</a>
                        </div>
                    </div>
                </div>
              )
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
