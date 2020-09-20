graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 15
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 2
    memory 10
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 165
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 179
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 198
  ]
  edge [
    source 1
    target 3
    delay 29
    bw 141
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 112
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 92
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 89
  ]
]
