graph [
  node [
    id 0
    label 1
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 5
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 57
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 85
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 198
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 70
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 130
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 64
  ]
]
