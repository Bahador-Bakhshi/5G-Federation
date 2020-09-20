graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 16
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 6
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 4
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 93
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 139
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 144
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 112
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 158
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 163
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 52
  ]
]
