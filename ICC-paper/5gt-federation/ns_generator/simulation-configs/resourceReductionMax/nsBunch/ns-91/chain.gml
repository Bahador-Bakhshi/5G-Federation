graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 4
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 5
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 188
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 163
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 109
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 96
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 141
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 103
  ]
]
