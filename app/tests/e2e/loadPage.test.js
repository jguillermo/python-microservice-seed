const request = require('@request');
const mysql = require('@mysql');

describe('Load Page', () => {

    test('leer la base de datos', async () => {
        let results = await mysql('SELECT 4 + 2 AS solution');
        expect(results[0].solution).toEqual(6);
    });

    test('carga del documento', async () => {
        let { body, statusCode } = await request('/doc');
        expect(statusCode).toEqual(200);
    });

    test('carga de la pagina Error', async () => {
        let { body, statusCode } = await request('/ruta/que/no/existe');
        expect(statusCode).toEqual(404);
        // expect(body).toEqual({ status: 404, url: '//xcvxcvxcv' });
    });


});
