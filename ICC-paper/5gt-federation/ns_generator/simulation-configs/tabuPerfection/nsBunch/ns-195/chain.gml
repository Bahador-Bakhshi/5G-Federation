graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 7
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
    disk 10
    cpu 2
    memory 2
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 5
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 8
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 118
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 159
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 161
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 185
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 80
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 106
  ]
]
