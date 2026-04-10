import boto3

def levantar_instancia():

    ec2 = boto3.client('ec2', region_name='us-east-1')

    print("Comienza el Proceso")
    try:
        respuesta = ec2.run_instances(
            ImageId='ami-0c7217cdde317cfec',
            InstanceType='t2.micro',
            MinCount=2,
            MaxCount=2,
            IamInstanceProfile={'Name': 'LabInstanceProfile'},
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'Instancia-Automatizada-DevOps'}]
            }]
        )

        print("Se creo las instancias")
        print("Los ID generados son:")

        for instancia in respuesta['Instances']:
            print(f" -- ID: {instancia['InstanceId']}")

    except Exception as e:
        print(f" Error al crea las instancias {e} ")

if __name__ == '__main__':
    levantar_instancia()
