graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 12
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 5
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 1
    memory 4
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 7
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 14
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 143
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 173
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 88
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 116
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 93
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 124
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 87
  ]
]
