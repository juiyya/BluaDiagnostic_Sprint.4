# POLÍTICA DE OPERAÇÃO E ATENDIMENTO EM TELEMEDICINA - CARE PLUS

## 1. ESCOPO DOS SERVIÇOS DIGITAIS
A plataforma de Telemedicina da Care Plus combina atendimento médico remoto via videoconferência com o monitoramento contínuo e inteligente de sinais vitais por meio de dispositivos wearables integrados.

### Modalidades de Atendimento:
- **Pronto Atendimento Digital (Assíncrono/Síncrono):** Triagem automatizada via IA com base nos sintomas relatados e telemetria atual. Casos críticos são imediatamente transferidos para a equipe médica de plantão.
- **Consultas Eletivas (Agendadas):** Consultas de rotina, acompanhamento de condições crônicas e emissão de receitas/relatórios.

## 2. DISPONIBILIDADE E ESPECIALIDADES MÉDICAS
- **Pronto Atendimento / Clínica Geral:** Disponibilidade integral, 24 horas por dia, 7 dias por semana (24/7), voltada para intercorrências agudas ou alertas de telemetria.
- **Cardiologia e Endocrinologia:** Atendimento ambulatorial eletivo mediante agendamento prévio, de segunda a sexta-feira, das 08h às 20h.
- **Saúde Mental (Psicologia e Psiquiatria):** Suporte especializado para manejo de crises, ansiedade e suporte contínuo.

## 3. REGRAS CRÍTICAS PARA AGENDAMENTO (SISTEMA)
O agente de agendamento (`schedule_agent`) deve obrigatoriamente seguir o fluxo de validação antes de confirmar qualquer teleconsulta:
1. **Validação de Identidade:** É mandatório coletar e confirmar o ID do paciente no banco de dados. Nenhuma consulta pode ser aberta sem um ID válido associado.
2. **Coleta de Parâmetros:** O usuário deve especificar e confirmar rigorosamente três variáveis: **Data**, **Horário** e **Especialidade** desejada.
3. **Bloqueio de Conflitos:** O sistema não permite o agendamento de duas consultas na mesma especialidade para o mesmo ID de paciente em intervalos menores que 24 horas.

## 4. INTEGRAÇÃO COM WEARABLES E DIRECIONAMENTO
- **Fluxo de Sinais Vitais:** Os dados coletados pelo wearable do paciente (como Frequência Cardíaca e Saturação de Oxigênio) são processados de forma assíncrona. 
- **Elegibilidade de Escalonamento:** Caso a triagem detecte parâmetros fora da normalidade (conforme o Protocolo de Manchester), o fluxo de agendamento regular é interrompido e o paciente é direcionado para a conduta de emergência ou plantão imediato.

## 5. EMISSÃO DE DOCUMENTOS MÉDICOS
Todas as receitas, atestados e pedidos de exames emitidos durante as teleconsultas utilizam assinatura digital padrão ICP-Brasil, possuindo validade legal em todo o território nacional. O agente de IA pode tirar dúvidas sobre medicamentos com base na base de conhecimento (RAG), mas nunca criará ou alterará prescrições de forma autônoma.