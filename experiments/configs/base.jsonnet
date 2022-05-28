local target_max_tokens = 200;

{
    "dataset_reader": {
        "type": "base_dataset_reader",
        "source_tokenizer": {
            "type": "pretrained_transformer",
            "model_name": "{model_name}",
        },
        "source_token_indexers": {
            "tokens": {
                "type": "pretrained_transformer",
                "model_name": "{model_name}",
                "namespace": "tokens",
            }
        },
        "source_max_tokens": 512,
        "target_max_tokens": target_max_tokens,
        "read_loops": 8,
        "n_train_sample": null,
        "n_test_sample": null,
        "sample_random_seed": 0
    },
    "model": {
        "type": "cfg_transformers",
        "model_name": "{model_name}",
        "beam_size": 2,
        "max_decoding_steps": target_max_tokens,
    },
    "data_loader": {
        "batch_sampler": {
            "type": "bucket",
            "batch_size": 28,  # t5-large will be overriden with smaller value
        }
    },
    "validation_data_loader": {
        "batch_sampler": {
         "type": "bucket",
         "batch_size": 24,  # t5-large will be overriden with smaller value
        }
    },
    "trainer": {
        "num_epochs": 8,
        "optimizer": {
            "type": "huggingface_adamw",
            "lr": 3e-5,
            "betas": [0.9, 0.999],
            "eps": 1e-8,
            "correct_bias": true,
        },
        "validation_metric": "+accuracy",
        "learning_rate_scheduler": {
            "type": "polynomial_decay",
        },
        "cuda_device": 0,
        "grad_norm": 1.0,
        "callbacks": [
            "save_predictions",
            "early_stopping",
        ],
        "checkpointer": {
            "save_completed_epochs": false
        },
        "run_confidence_checks": false
    }
}