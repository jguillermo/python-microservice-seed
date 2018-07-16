/**
 *
 * Modo de uso :
 *
 * const mysql = require('@mysql');
 *
let results = await mysql('SELECT 4 + 2 AS solution');
expect(results[0].solution).toEqual(6);
 */

require('./config');
var mysql = require('mysql');
function getConnection() {
    //'mysql://user:pass@host:port/dbname';
    let connection = mysql.createConnection(process.env.DATABASE);
    connection.connect();
    return connection;
}

function query(sql) {
    return new Promise(function (resolve, reject){
        let  conection = getConnection();
        conection.query(sql, function (error, results, fields) {
            if (error) {
                console.log('env.DATABASE',process.env.DATABASE,'conection',conection.config,'**error**',error,'**throw error**');
                throw error;
                reject(error);
            }
            conection.destroy();
            resolve(results);
        });
      });
}

module.exports = query;
