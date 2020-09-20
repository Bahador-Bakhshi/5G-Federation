graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 1
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 172
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 189
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 144
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 109
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 155
  ]
  edge [
    source 2
    target 5
    delay 27
    bw 197
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 161
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 86
  ]
]
