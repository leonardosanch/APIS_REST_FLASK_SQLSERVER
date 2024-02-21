

CREATE PROCEDURE SP_L_EMPLEADOS_01
AS
BEGIN

	SELECT EmployeeID,LastName,FirstName,Title,Address  from Employees 
	
END

EXEC SP_L_EMPLEADOS_01

SELECT  * from tm_usuario

CREATE  PROCEDURE SP_L_USUARIO_01

AS 
BEGIN 
	SELECT  * FROM tm_usuario
	WHERE 
	est=1
END

EXEC SP_L_USUARIO_01







CREATE  PROCEDURE SP_L_USUARIO_02
@usu_id  INT

AS 
BEGIN 
	SELECT  * FROM tm_usuario
	WHERE 
		usu_id = @usu_id
END

EXEC SP_L_USUARIO_02 3




CREATE PROCEDURE SP_I_USUARIO_01
@usu_nom varchar(50),
@usu_correo varchar(90)

AS
BEGIN

INSERT INTO tm_usuario(usu_nom,usu_correo) values(@usu_nom,@usu_correo)
END


EXEC SP_I_USUARIO_01 'xlx', 'xlx@gmail.com'




CREATE PROCEDURE SP_U_USUARIO_01
@usu_id int,
@usu_nom varchar(50),
@usu_correo varchar(90)

AS
BEGIN
UPDATE  tm_usuario 
SET 
	usu_nom = @usu_nom,
	usu_correo = @usu_correo
WHERE 
	usu_id  = @usu_id
END 


EXEC  SP_U_USUARIO_01 5, 'updateperiquito', 'test5@test.com'

SELECT *from tm_usuario 




CREATE PROCEDURE SP_D_USUARIO_01
@usu_id INT
AS
BEGIN
	UPDATE tm_usuario
	SET 
	est=0
	WHERE 
		usu_id=@usu_id
END 

EXEC SP_D_USUARIO_01 4


