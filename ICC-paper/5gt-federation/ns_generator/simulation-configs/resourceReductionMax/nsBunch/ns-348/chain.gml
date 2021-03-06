graph [
  node [
    id 0
    label 1
    disk 8
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 4
    memory 16
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 1
    memory 15
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
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
    bw 102
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 63
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 51
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 119
  ]
  edge [
    source 2
    target 3
    delay 28
    bw 109
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 102
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 128
  ]
]
