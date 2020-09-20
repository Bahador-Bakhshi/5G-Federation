graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 2
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 16
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 114
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 181
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 193
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 197
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 98
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 126
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 189
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 57
  ]
]
