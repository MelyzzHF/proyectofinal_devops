import boto3

def generar_reporte():

    ec2 = boto3.client('ec2', region_name='us-east-1')
    s3 = boto3.client('s3', region_name='us-east-1')

    print("- REPORTE AUTOMÁTICO DE RECURSOS AW-")
    print("\n INSTANCIAS EC2 ACTUALES:")
    try:
        instancias = ec2.describe_instances()
        for reserva in instancias['Reservations']:
            for inst in reserva['Instances']:

                print(f" - ID: {inst['InstanceId']} | Estado: {inst['State']['Name']}")
    except Exception as e:
        print(" Error al consultar EC")

    print("\n BUCKETS S3 ACTUALES Y SUS OBJETOS:")
    try:
        buckets = s3.list_buckets()
        if not buckets['Buckets']:
            print(" - No hay buckets creados actualmente.")
        else:
            for b in buckets['Buckets']:
                nombre_bucket = b['Name']
                print(f" Bucket: {nombre_bucket}")

                try:
                    objetos = s3.list_objects_v2(Bucket=nombre_bucket)
                    if 'Contents' in objetos:
                        for obj in objetos['Contents']:
                            print(f" Archivo: {obj['Key']} ({obj['Size']} bytes)")
                    else:
                        print("El bucket está vacío.")
                except Exception as e_obj:
                    print(f" No se pudieron leer los objetos: {e_obj}")
    except Exception as e:
        print(f" Error al consultar S3: {e}"
)
    print("Reporte finalizado.")

if __name__ == '__main__':
    generar_reporte()
