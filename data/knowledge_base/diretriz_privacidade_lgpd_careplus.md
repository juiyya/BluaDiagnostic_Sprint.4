# DIRETRIZ DE PRIVACIDADE E CONFORMIDADE LGPD - CARE PLUS

## 1. ESCOPO E TRATAMENTO DE DADOS SENSÍVEIS
A Care Plus atua no tratamento de dados pessoais e dados pessoais sensíveis (dados de saúde e telemetria médica), em estrita conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).

### Dados Coletados pelo Sistema:
- **Dados Cadastrais:** Nome, idade e Identificador Único do Paciente (ID).
- **Dados de Saúde (Sensíveis):** Histórico clínico, prontuários, alergias, uso de medicamentos contínuos e logs de consultas.
- **Dados de Telemetria (Sensíveis/Wearables):** Sinais vitais coletados em tempo real (Frequência Cardíaca e Saturação de Oxigênio - SpO2).

## 2. BASES LEGAIS PARA O TRATAMENTO
O tratamento dos dados de saúde e telemetria dentro da plataforma fundamenta-se nas seguintes bases legais da LGPD:
1. **Tutela da Saúde (Art. 7º, VIII e Art. 11, II, "f"):** Para procedimentos realizados por profissionais de saúde e serviços de saúde integrados.
2. **Execução de Contrato (Art. 7º, V):** Para a prestação dos serviços de telemedicina e monitoramento contratados pelo beneficiário.
3. **Proteção da Vida ou da Incolumidade Física (Art. 7º, VII e Art. 11, II, "e"):** Aplicada estritamente pelo agente de escalonamento em cenários de Alerta Vermelho/Emergência médica.

## 3. RETENÇÃO, ARMAZENAMENTO E SEGURANÇA
- **Segurança Criptográfica:** Todos os dados de sinais vitais e prontuários devem ser criptografados em trânsito e em repouso.
- **Restrição de Acesso:** Os agentes de IA operam sob o princípio do privilégio mínimo. O acesso ao histórico clínico por qualquer agente é estritamente proibido sem a validação prévia e confirmação do ID do paciente.
- **Retenção:** Os dados de prontuário e histórico de atendimento são mantidos pelo prazo mínimo legal exigido pelo Conselho Federal de Medicina (CFM) e legislações de arquivamento médico vigentes.

## 4. DIREITOS DO TITULAR E REGRAS DOS AGENTES (IA)
- **Transparência:** Os agentes inteligentes não devem mascarar logs ou omitir do paciente quais dados estão sendo consultados quando solicitados legítimamente.
- **Exclusão de Dados:** O paciente pode solicitar a revogação de consentimentos periféricos, disparando a rotina de exclusão ou anonimização dos dados de telemetria que não estejam sob obrigação legal de retenção médica.