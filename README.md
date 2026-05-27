# ProyectoXAI

El orden de ejecución de los archivos es el siguiente:

1. teacher_finetuning.ipynb
    ---> Se obtiene como resultado el modelo profesor.

2. student_training.ipynb / student_local_training.ipynb
    ---> El orden de ejecución entre ellos es irrelevante
    ---> Se obtiene como resultado los modelos estudiante

3. model_functional_eval_and_compare.ipynb / model_representational_comparisons.ipynb
    ---> El orden de ejecución entre ellos es irrelevante
    ---> Se obtiene como resultado las métricas de evaluación y comparación entre modelos estudiantes-profesor y estudiante-estudiante
