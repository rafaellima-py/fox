import stripe
from decouple import config
stripe.api_key = config("STRIPE_PROD")


language = {
    "espanhol": {
        "inicio": """ 
💎INCESTO+18 🫦
💎AMAMANTAR AL HIJO‼️
💎 CONTENIDO RESTRINGIDO 😈
💎 Celebridades FAMOSAS FILTRADAS 👀
💎 NUEVAS 18+ 👅
💎AFICIONADO 🔥
💎 CONTROVERSIAL +18 🥵
💎 MILF 👵🏻
💎VIDAS🎬
💎FAVELADAS🔥
💎ANAL 😈
💎MAMADAS 👄""",
        "inicio2": "¡Hola, Bienvenido de nuevo 🙂",
        "produtos": "🎟️ Productos disponibles 🎟️",
        "call_interesse": "Estás interessado en unirtre al mejor canal de putas del mundo ?",
        "cb_nao_interesse": "¡Gracias por tu interés, hasta luego  😉",
        "pg_instrucao": "Realiza el pago y envía una foto del comprobante; este será enviado para la aprobación de un administrador, y recibirás un enlace de acceso después de la aprobación",
        "oferta_semanal": "Sigue con el plan semanal",
        'oferta_exclusiva': "Quiero una oferta exclusiva",
        "oferta_apresentacao": "Tenemos una oferta exclusiva para ti  Paga una semana más y recibe dos semanas gratis\n\n Recibirás en total: 1 mes de acceso por €16,00",
        "obrigado": 'Gracias por suscribirse',
        '5dias': 'Su suscripción caducará en 5 días. Vuelve a firmar un plan. /start',
        '4dias': 'Su suscripción caducará en 4 días. Vuelve a firmar un plan. /start',
        '3dias': 'Su suscripción caducará en 3 días. Vuelve a firmar un plan. /start',
        '2dias': 'Su suscripción caducará en 2 días. Vuelve a firmar un plan. /start',
        '1dias': 'Su suscripción caducará en 1 dia. Vuelve a firmar un plan. /start',
        '3min': 'Su suscripción caducará en 30 min. Vuelve a firmar un plan. /start.',
        'expirado': 'Su suscripción ha caducado. Vuelve a firmar un plan. /start.',
        'cta1': 'Quiero suscribirme al vip € 8,00 🔞',
        'plano': 'Elige tu plan',
        'mensal': '🔞 Mensual € 25.99',
        'semanal': '🔥 Semanal € 15.99',
        'trimestral': '😈 Trimestral € 38.99',
        'mbway': 'Pagar con Mbway',
        'mbway': 'Pagar con Mbway',
        'bizum': 'Pagar con Bizum',
        'esperando_pg': 'Esperando pago...'
    }, 
    
    "portugues": {
        "inicio": """
💎INCESTO+18 🫦
💎MAMANDO O FILHO‼️
💎 CONTEÚDO RESTRITO 😈
💎 VAZADOS DE FAMOSAS 👀
💎 NOVINHAS +18 👅
💎 AMADOR 🔥
💎 POLÊMICOS +18 🥵
💎 MILF 👵🏻
💎 LIVES 🎬
💎 FAVELADAS 🔥
💎 ANAL 😈
💎 BOQUETES 👄
""",
        "inicio2": "Olá, Bem Vindo de volta 🙂",
        "produtos": "🎟️ Produtos disponíveis 🎟️",
        "call_interesse": "Tem interesse em entrar no melhor canal de putaria do mundo",
        "cb_nao_interesse": "Obrigado pelo seu interesse, até mais  😉",
        "pg_instrucao": "Realize o pagamento e envie foto do comprovante, ele será envirado para a aprovação de um administrador você receberá um link de acesso após a aprovação",
        "oferta_semanal": "Siga com o plano semanal",
        "oferta_exclusiva": "Quero uma oferta exclusiva",
        "oferta_apresentacao": "Temos uma oferta exclusiva para você: Pague mais uma semana e receba mais duas semanas gratís\n\n Você receberá no total: 1 mês de acesso por €16,00",
        "obrigado": 'Obrigado por se inscrever',
        "5dias": 'Sua assinatura expirará em 5 dias. Assine um plano novamente /start.',
        "4dias": 'Sua assinatura expirará em 4 dias. Assine um plano novamente /start.',
        "3dias": 'Sua assinatura expirará em 3 dias. Assine um plano novamente /start.',
        "2dias": 'Sua assinatura expirará em 2 dias. Assine um plano novamente /start.',
        "1dias": 'Sua assinatura expirará em 1 dia. Assine um plano novamente /start.',
        '3min': 'Sua assinatura expirará em 30 minutos. Assine um plano novamente /start.',
        'expirado': 'Sua assinatura expirou. Assine um plano novamente /start.',
        'cta1': 'Quero assinar o vip € 8,00 🔞',
        'plano': 'Escolha seu plano',
        'mensal': '🔞 Mensal € 25.99',
        'semanal': '🔥 Semanal € 15.99',
        'trimestral': '😈 Trimestral € 38.99',
        'mbway': 'Pagar com Mbway',
        'bizum': 'Pagar com Bizum',
        'esperando_pg': 'Esperando pagamento...'
    },
    
    "ingles": {
        "inicio": """
💎INCEST+18 🫦
💎BREASTFEEDING THE SON‼️
💎 RESTRICTED CONTENT 😈
💎 LEAKED FAMOUS Celebrities 👀
💎 NEW 18+ 👅
💎 AMATEUR 🔥
💎 CONTROVERSIAL +18 🥵
💎 MILF 👵🏻
💎 LIVES 🎬
💎 brazil favela 🔥
💎 taking it up the ass 😈
💎 BLOWJOBS 👄        
""",
        "inicio2": "Hello, Welcome back 🙂",
        "produtos": "🎟️ Available products 🎟️",
        "call_interesse": "Are you interested in joining the best adult content channel in the world?",
        "cb_nao_interesse": "Thanks for your interest, see you later 😉",
        "pg_instrucao": "Make the payment and send a photo of the receipt; it will be sent for approval by an administrator, and you will receive an access link after approval.",
        "oferta_semanal": "Follow the weekly plan",
        "oferta_exclusiva": "I want an exclusive offer",
        "oferta_apresentacao": "We have an exclusive offer for you: Pay for one more week and get two additional weeks for free.\n\n You will receive in total: 1 month of access for €16.00",
        "obrigado": 'Thank you for subscribing, visit our website: www.dopaminas.com',
        "5dias": 'Your subscription will expire in 5 days. Renew a plan /start.',
        "4dias": 'Your subscription will expire in 4 days. Renew a plan /start.',
        "3dias": 'Your subscription will expire in 3 days. Renew a plan /start.',
        "2dias": 'Your subscription will expire in 2 days. Renew a plan /start.',
        "1dias": 'Your subscription will expire in 1 day. Renew a plan /start.',
        '3min': 'Your subscription will expire in 30 minutes. Renew a plan /start.',
        'expirado': 'Your subscription has expired. Renew a plan /start.',
        'cta1': 'I want to subscribe to the VIP €8.00 🔞',
        'plano': 'Choose your plan',
        'mensal': 'Monthly',
        'semanal': 'Weekly',
        'trimestral': 'Quarterly',

    }
}


preco_pt = [
    9.90,
    16.90,
    22.90,
    37.90,

]
preco_es = [
    11.90,
    16.90,
    24.90,
    49.90,
    
]
produtos = stripe.Product.list()


def formatar_moeda(preco, moeda):
    simbolos = {"usd": "$", "brl": "R$", "eur": "€"}
    return f"{simbolos.get(moeda, moeda)}{preco:.2f}"



def show_product_pt():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": preco.data[0].id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        if preco.data[0].unit_amount / 100 in preco_pt:
            if produto.images:
                dictn = {"prod_id": produto.id,"nome": produto.name, "imagem": produto.images[0],
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         "url": checkout.url, "id_checkout": checkout.id}
                
                resultado.append(dictn)
                
            else:
                dictn = {"prod_id": produto.id,"nome": produto.name,
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         "url": checkout.url, "id_checkout": checkout.id}
                
                resultado.append(dictn)
    return resultado



def show_product_es():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": preco.data[0].id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        if preco.data[0].unit_amount / 100 in preco_es:
            if produto.images:
                dictn = {"prod_id": produto.id, "nome": produto.name, "imagem": produto.images[0],
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency), "url": checkout.url}
                resultado.append(dictn)
                
            else:
                dictn = {"prod_id": produto.id,"nome": produto.name, "moeda": formatar_moeda(preco.data[0].unit_amount / 100, "usd"), "url": checkout.url}
                resultado.append(dictn)
    return resultado

def single_product(prod_id):
    produto = stripe.Product.retrieve(prod_id)
    preco = stripe.Price.list(product=produto.id)
    checkout = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": preco.data[0].id,
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )
    if produto.images:
        dictn = {"prod_id": produto.id, "nome": produto.name, "imagem": produto.images[0],
                 "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 "url": checkout.url, "id_checkout": checkout.id, "preco": preco.data[0].unit_amount / 100}
        return dictn
    else:
        dictn = {"prod_id": produto.id,"nome": produto.name, "imagem": None,
                 "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 "url": checkout.url, "id_checkout": checkout.id, "preco": preco.data[0].unit_amount / 100}
        return dictn


def dict_plain(idioma):
    if idioma == "espanhol":
        plain = {11.90: "semanal", 16.90: "mensal", 24.90: "bimestral", 49.90: "vitalicio"}
    elif idioma == "portugues":
        plain = {9.90: "semanal", 16.90: "mensal", 22.90: "bimestral", 37.90: "vitalicio"}
    return plain
#print((single_product("prod_QuvWYoJ6uKPzB3")))