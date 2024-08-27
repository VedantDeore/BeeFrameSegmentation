import torch
import torchvision
from torchvision.ops import box_iou
from sklearn.metrics import f1_score

# Function to compute mAP for segmentation
def compute_map(pred_boxes, pred_labels, pred_scores, true_boxes, true_labels, iou_threshold=0.5):
    """
    Computes mean Average Precision (mAP) for object detection.
    
    Parameters:
    - pred_boxes: List of predicted bounding boxes for all images
    - pred_labels: List of predicted labels for all images
    - pred_scores: List of predicted scores for all images
    - true_boxes: List of ground truth bounding boxes for all images
    - true_labels: List of ground truth labels for all images
    - iou_threshold: IOU threshold for a positive match
    
    Returns:
    - mAP value
    """
    aps = []
    for i in range(len(true_boxes)):
        # Convert to tensors
        pred_b = torch.tensor(pred_boxes[i], dtype=torch.float32)
        true_b = torch.tensor(true_boxes[i], dtype=torch.float32)
        pred_s = torch.tensor(pred_scores[i], dtype=torch.float32)

        if len(pred_b) == 0 or len(true_b) == 0:
            aps.append(0)
            continue

        # Compute IoU
        ious = box_iou(pred_b, true_b)

        # Sort predictions by score
        sorted_indices = torch.argsort(pred_s, descending=True)
        ious = ious[sorted_indices]

        # Calculate True Positives and False Positives
        tp = (ious >= iou_threshold).sum(dim=1).clamp(max=1)
        fp = 1 - tp

        # Calculate Precision and Recall
        tp_cumsum = torch.cumsum(tp, dim=0)
        fp_cumsum = torch.cumsum(fp, dim=0)
        recall = tp_cumsum / (len(true_b) + 1e-5)
        precision = tp_cumsum / (tp_cumsum + fp_cumsum + 1e-5)

        # Calculate AP (Average Precision)
        ap = torch.trapz(precision, recall)
        aps.append(ap.item())

    # Mean Average Precision
    return sum(aps) / len(aps)

# Function to compute F1-Score for segmentation
def compute_f1(true_masks, pred_masks, threshold=0.5):
    """
    Computes F1-Score for segmentation.
    
    Parameters:
    - true_masks: Ground truth masks for all images
    - pred_masks: Predicted masks for all images
    - threshold: Threshold for binary classification
    
    Returns:
    - F1-Score value
    """
    true_flat = torch.flatten(torch.tensor(true_masks, dtype=torch.int))
    pred_flat = torch.flatten((torch.tensor(pred_masks) > threshold).int())
    f1 = f1_score(true_flat.cpu().numpy(), pred_flat.cpu().numpy())
    return f1

# Example Usage
pred_boxes = [[[0, 0, 100, 100]], [[50, 50, 150, 150]]]  # Example predicted boxes for 2 images
pred_labels = [[1], [1]]  # Example predicted labels for 2 images
pred_scores = [[0.9], [0.8]]  # Example predicted scores for 2 images
true_boxes = [[[0, 0, 95, 95]], [[55, 55, 145, 145]]]  # Example true boxes for 2 images
true_labels = [[1], [1]]  # Example true labels for 2 images
pred_masks = [torch.rand(1, 224, 224), torch.rand(1, 224, 224)]  # Example predicted masks
true_masks = [torch.rand(1, 224, 224), torch.rand(1, 224, 224)]  # Example true masks

# Calculate mAP
map_value = compute_map(pred_boxes, pred_labels, pred_scores, true_boxes, true_labels)
print(f"Mean Average Precision (mAP): {map_value:.4f}")

# Calculate F1-Score
f1_value = compute_f1(true_masks, pred_masks)
print(f"F1-Score: {f1_value:.4f}")
