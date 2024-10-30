from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reativacao, IdIccid

@receiver(post_save, sender=IdIccid)
def enviar_email_requisicao_criada(sender, instance, created, **kwargs):
    if created:
        # Obter detalhes do IdIccid recém-criado
        id_iccid_details = f"ID: {instance.id_equipamentos}, ICCID: {instance.ccid_equipamentos}"
        
        subject = f"Novo Equipamento Reativado: {instance.id_equipamentos}"
        message = f"""
        Um novo equipamento foi reativado com os seguintes detalhes:
        
        Detalhes do Equipamento:
        {id_iccid_details}
        """

        from_email = 'sysggoldensat@gmail.com'
        recipient_list = ['sjuniorr6@gmail.com']

        send_mail(subject, message, from_email, recipient_list)
