graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 5
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 182
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 128
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 93
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 154
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 79
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 87
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 57
  ]
]
