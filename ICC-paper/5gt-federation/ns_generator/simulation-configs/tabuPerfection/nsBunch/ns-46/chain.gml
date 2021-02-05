graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 3
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 10
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 8
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 10
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 54
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 174
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 54
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 170
  ]
  edge [
    source 1
    target 5
    delay 32
    bw 155
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 141
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 56
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 185
  ]
]
