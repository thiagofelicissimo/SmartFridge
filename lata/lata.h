#ifndef LATA_H
#define LATA_H


#include "msp430g2553.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "general.h"
#include "uart.h"


typedef struct lat
{
	// canal_temperatura guarda o bit correspondente ao canal utilizado para cada medicao
	// tempfinal armazena a temperatura apos o tratamento da amostra de 20 medicoes, armazenada em amostra[20]
	// medic_feitas guarda o numero de medicoes feitas ate o momento e presenca_flag indica se a lata esta presente
	// durante todo o processo de medicao (condicao para a amostra ser tratada)
	// porta_presenca guarda o numero da porta utilizada para verificar a presenca (ex. 21 se refere a porta 2_1)
	unsigned int canal_temperatura;
	int tempfinal, medic_feitas, presenca_flag, porta_presenca; // presenca_flag = 1 <=> lata ficou ausente durante a medicao
	unsigned int id; // so 2 bit
	char ultimo_TX[3]; // guarda string da ultima mensagem enviada
	int amostra[20];									
} lt;

int LATA_MedicaoValida (unsigned int a);

void LATA_Resetar (lt *lp);

void LATA_Iniciar (unsigned int tempcanal, int presscanal, lt *lp, unsigned int identific);

void LATA_Enviar (lt* lp);

int LATA_CarregarMedicoes (lt* lp, unsigned int medicoes[]);

unsigned int LATA_PegarCanais (lt* lp);

int LATA_VerificarPresenca (int canal);

#endif